import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import java.util.StringTokenizer;

public class BiGrInvInd {

    public static class BiGrInvIndMapper extends Mapper<Object, Text, Text, Text> {

        private final Text id = new Text(), bigram = new Text();

        @Override
        protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] doc = value.toString().split("\\t", 2);
            String content = doc[1].toLowerCase().replaceAll("[^a-z]+", " ");
            StringTokenizer tokenizer = new StringTokenizer(content, " ");
            String prev = tokenizer.nextToken(), cur;
            id.set(doc[0]);
            while (tokenizer.hasMoreTokens()) {
                cur = tokenizer.nextToken();
                bigram.set(prev + " " + cur);
                context.write(bigram, id);
                prev = cur;
            }
        }
    }

    public static class BiGrInvIndReducer extends Reducer<Text, Text, Text, Text> {

        @Override
        public void reduce(Text bigram, Iterable<Text> idLs, Context context) throws IOException, InterruptedException {
            Map<String, Integer> fMap = new HashMap<>();
            for (Text id : idLs) {
                String idStr = id.toString();
                fMap.put(idStr, fMap.getOrDefault(idStr, 0) + 1);
            }

            StringBuilder freqBuilder = new StringBuilder();
            for (Map.Entry<String, Integer> entry : fMap.entrySet()) {
                if (freqBuilder.length() > 0) {
                    freqBuilder.append(" ");
                }
                freqBuilder.append(String.format("%s:%d", entry.getKey(), entry.getValue()));
            }
            context.write(bigram, new Text(freqBuilder.toString()));
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
        if (args.length != 2) {
            System.err.println("Usage: Bigrams Inverted Index <input path> <output path>");
            System.exit(-1);
        }
        String inputFile = args[0];
        String outputFile = args[1];

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Bigrams Inverted Index");
        job.setJarByClass(BiGrInvInd.class);
        job.setMapperClass(BiGrInvIndMapper.class);
        job.setReducerClass(BiGrInvIndReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        Path inputFilePath = new Path(inputFile);
        Path outputFilePath = new Path(outputFile);
        FileSystem fileSystem = outputFilePath.getFileSystem(conf);
        if (fileSystem.exists(outputFilePath)) {
            fileSystem.delete(outputFilePath, true);
        }
        FileInputFormat.addInputPath(job, inputFilePath);
        FileOutputFormat.setOutputPath(job, outputFilePath);

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}