import java.io.*;
import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;

class Basic {
    public static String[] stringGenerator(String filePath) throws IOException {
        String longStrA = "", longStrB = "";
        String[] str = new String[2];
        InputStream is = new FileInputStream(filePath);
        String strTempA, strTempB;
        int i, insertIndex;
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        strTempA = reader.readLine();
        String nextA = "", nextB = "";
        i=0;
        while(true) {
            nextA = reader.readLine();
            if(nextA.chars().allMatch( Character::isDigit)) {
                insertIndex = Integer.valueOf(nextA);
                longStrA = strTempA.substring(0, insertIndex + 1).concat(strTempA).concat(strTempA.substring(insertIndex + 1));
                strTempA = longStrA;
            }else {
                if(i==0){
                    longStrA = strTempA;
                }
                break;
            }
            i++;
        }
        strTempB = nextA;
        i=0;
        while(true){
            nextB = reader.readLine();
            if(nextB!=null) {
                insertIndex = Integer.valueOf(nextB);
                longStrB = strTempB.substring(0, insertIndex + 1).concat(strTempB).concat(strTempB.substring(insertIndex + 1));
                strTempB = longStrB;
            }else {
                if(i==0){
                    longStrB = strTempB;
                }
                break;
            }
            i++;
        }

        str[0]=longStrA;
        str[1]=longStrB;
        reader.close();
        is.close();
        return str;
    }

    public static void main(String args[]) throws IOException {
        if(args.length != 1){
            return;
        }
        int cost;
        long memoryUsageBefore, memoryUsageAfter;
        double cpuTimeBefore, cpuTimeAfter;
        
        //Start
        ThreadMXBean stat = ManagementFactory.getThreadMXBean();
        memoryUsageBefore = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        cpuTimeBefore = stat.getCurrentThreadCpuTime()/1000000000.0;

        String[] str = stringGenerator(args[0]);
        String A = str[0], B = str[1];
        BasicAlignment bsAlign = new BasicAlignment();

        //basic ver.
        cost = bsAlign.SequenceAlign(A, B);
        cpuTimeAfter = stat.getCurrentThreadCpuTime()/1000000000.0;
        memoryUsageAfter = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

        File fout = new File("output.txt");
        if(fout.exists()){
            fout.delete();
        }
        fout.createNewFile();
        BufferedWriter output = new BufferedWriter(new FileWriter(fout));
        output.write(bsAlign.resArray.get(0).substring(0, Math.min(50, bsAlign.resArray.get(0).length())) + " " + bsAlign.resArray.get(0).substring(Math.max(0, bsAlign.resArray.get(0).length() - 50), bsAlign.resArray.get(0).length()) + "\n");
        output.write(bsAlign.resArray.get(1).substring(0, Math.min(50, bsAlign.resArray.get(1).length())) + " " + bsAlign.resArray.get(1).substring(Math.max(0, bsAlign.resArray.get(1).length() - 50), bsAlign.resArray.get(1).length()) + "\n");
        output.write(String.valueOf((double)cost) + "\n");
        //memory
        output.write(String.valueOf((memoryUsageAfter-memoryUsageBefore)/(1024.0)) + "\n");
        //time
        output.write(String.valueOf(cpuTimeAfter-cpuTimeBefore));
        output.close();

    }
}
