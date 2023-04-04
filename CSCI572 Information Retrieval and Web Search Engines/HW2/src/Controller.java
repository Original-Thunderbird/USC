import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;

import edu.uci.ics.crawler4j.crawler.CrawlConfig;
import edu.uci.ics.crawler4j.crawler.CrawlController;
import edu.uci.ics.crawler4j.fetcher.PageFetcher;
import edu.uci.ics.crawler4j.robotstxt.RobotstxtConfig;
import edu.uci.ics.crawler4j.robotstxt.RobotstxtServer;

public class Controller {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		CrawlConfig config = new CrawlConfig();
		
		config.setCrawlStorageFolder("/data/crawl");
		config.setMaxDepthOfCrawling(16);
		config.setMaxPagesToFetch(20000);
		config.setPolitenessDelay(300);
        config.setUserAgentString("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36");
        config.setIncludeBinaryContentInCrawling(true);
		
		/*
		* Instantiate the controller for this crawl.
		*/
		PageFetcher pageFetcher = new PageFetcher(config);
		RobotstxtConfig robotstxtConfig = new RobotstxtConfig();
		RobotstxtServer robotstxtServer = new RobotstxtServer(robotstxtConfig, pageFetcher);
		CrawlController controller = new CrawlController(config, pageFetcher, robotstxtServer);
		/*
		* For each crawl, you need to add some seed urls. These are the first
		* URLs that are fetched and then the crawler starts following links
		* which are found in these pages
		*/
		controller.addSeed("https://www.wsj.com");
		/*
		* Start the crawl. This is a blocking operation, meaning that your code
		* will reach the line after this only when crawling is finished.
		*/
		controller.start(MyCrawler.class, 6);
		
	}

	
	private static void writeStat(String out, String s) throws IOException {
        PrintWriter writer = new PrintWriter(new FileOutputStream(s, false));
        writer.println(out.trim());
        writer.close();
    }
}
