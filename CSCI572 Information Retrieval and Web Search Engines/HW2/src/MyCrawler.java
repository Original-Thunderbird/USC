import java.util.Set;
import java.util.regex.Pattern;
import com.opencsv.CSVWriter;
import java.io.FileWriter;
import java.io.IOException;

import edu.uci.ics.crawler4j.crawler.Page;
import edu.uci.ics.crawler4j.crawler.WebCrawler;
import edu.uci.ics.crawler4j.parser.BinaryParseData;
import edu.uci.ics.crawler4j.parser.HtmlParseData;
import edu.uci.ics.crawler4j.url.WebURL;

public class MyCrawler extends WebCrawler {
	private final static Pattern FILTERS = Pattern.compile(".*(\\.(" + "wav|avi|mov|mpeg|mpg|ram|m4v|wma|wmv|css|js|json|zip|rar|gz|ttf|svg|mid|txt|mp2|mp3|mp4|exe))$");
	//private final static Pattern POOL = Pattern.compile(".*(\\.(" + "htm|html|pdf|doc|docx|avif|bmp|gif|ico|jpg|jpeg|png|svg|tif|tiff|webp))$");
	
	int count = 0;
	
	private static CSVWriter fetchWriter;
    private static CSVWriter visitWriter;
    private static CSVWriter urlsWriter;
	
    public MyCrawler() throws Exception{
        fetchWriter = new CSVWriter(new FileWriter("fetch_wsj.csv"));
        visitWriter = new CSVWriter(new FileWriter("visit_wsj.csv"));
        urlsWriter = new CSVWriter(new FileWriter("urls_wsj.csv"));
        fetchWriter.writeNext(new String[]{"URL","Status"});
        visitWriter.writeNext(new String[]{"URL","Size","# of Outlinks","Content-Type"});
        urlsWriter.writeNext(new String[]{"URL","URL Type"});
    }
    
	/**
	* This method receives two parameters. The first parameter is the page
	* in which we have discovered this new url and the second parameter is
	* the new url. You should implement this function to specify whether
	* the given url should be crawled or not (based on your crawling logic).
	* In this example, we are instructing the crawler to ignore urls that
	* have css, js, git, ... extensions and to only accept urls that start
	* with "http://www.viterbi.usc.edu/". In this case, we didn't need the
	* referringPage parameter to make the decision.
	*/
	@Override
	public boolean shouldVisit(Page referringPage, WebURL url) {
		String trimmedURL = url.getURL().toLowerCase();
		if(!trimmedURL.startsWith("https://www.wsj.com") && !trimmedURL.startsWith("http://www.wsj.com")) {
			String [] rowStrings = {url.getURL().replace(",", "-"), "N_OK"};
            urlsWriter.writeNext(rowStrings);
			return false;
		}
		String [] rowStrings = {url.getURL().replace(",", "-"), "OK"};
        urlsWriter.writeNext(rowStrings);
		return !FILTERS.matcher(trimmedURL).matches();
	}
	
	/**
	* This function is called when a page is fetched and ready
	* to be processed by your program.
	*/
	@Override
	public void visit(Page page) {
		String url = page.getWebURL().getURL().toLowerCase().replace(",", "-");
		int fileSize = page.getContentData().length;
		int numLink = 0;
		Set<WebURL> links;
		
		String type = page.getContentType().split(";")[0];
		boolean typeCheck = type.contains("html") | type.contains("image") | 
				type.contains("application/vnd.openxmlformats-officedocument.wordprocessingml.document") | type.contains("msword") | type.contains("pdf");
		if(!typeCheck) {
			return;
		}
		
		count++;
		System.out.println(count + " URL: " + url);
		
		if (page.getParseData() instanceof HtmlParseData) {
			HtmlParseData htmlParseData = (HtmlParseData) page.getParseData();
			links = htmlParseData.getOutgoingUrls();
			numLink = links.size();
		}
		else {
			BinaryParseData binaryParseData = (BinaryParseData) page.getParseData();	
			links = binaryParseData.getOutgoingUrls();
			numLink = links.size();
		}
		
		String [] rowStrings = {url, String.valueOf(fileSize), String.valueOf(numLink), type};
        visitWriter.writeNext(rowStrings);
	}
	
	@Override
	protected void handlePageStatusCode(WebURL webUrl, int statusCode, String statusDescription) {
		String href = webUrl.getURL().replace(",", "-");
		String [] rowStrings = {href, String.valueOf(statusCode)};
        fetchWriter.writeNext(rowStrings);
    }
	
	@Override
    public void onBeforeExit() {
        super.onBeforeExit();
        try {
            fetchWriter.close();
            visitWriter.close();
            urlsWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
