import javax.management.ObjectName;
import java.io.*;
import java.lang.management.ManagementFactory;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;
import java.util.ArrayList;
import java.util.Arrays;


class Efficient {

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
        int i, cost, resLen;
        long memoryUsageBefore, memoryUsageAfter;
        double cpuTimeBefore, cpuTimeAfter;
        
        //start
        ThreadMXBean stat3 = ManagementFactory.getThreadMXBean();
        memoryUsageBefore = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        cpuTimeBefore = stat3.getCurrentThreadCpuTime()/1000000000.0;

        String[] str = stringGenerator(args[0]);
        String A = str[0], B = str[1];

        EfficientAlignment efAlign = new EfficientAlignment();

//        //DCAlign Ver.1
//        ThreadMXBean stat2 = ManagementFactory.getThreadMXBean();
////        System.out.println(Runtime.getRuntime().totalMemory());
////        System.out.println(Runtime.getRuntime().freeMemory());
//        memoryUsageBefore = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
////        System.out.println("before enter: " + memoryUsageBefore);
//        cpuTimeBefore = stat2.getCurrentThreadCpuTime()/1000000000.0;
//
//        ArrayList<StringBuilder> list2 = efAlign.DcAlign(A,B);
//
//        cpuTimeAfter = stat2.getCurrentThreadCpuTime()/1000000000.0;
////        System.out.println(Runtime.getRuntime().totalMemory());
////        System.out.println(Runtime.getRuntime().freeMemory());
//        memoryUsageAfter = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
////        System.out.println("after quit: " + memoryUsageAfter);
////        System.out.println("Total Memory Used: " + (memoryUsageAfter-memoryUsageBefore)/(1024.0));
////        System.out.println("Total CPU Used is: " + (cpuTimeAfter-cpuTimeBefore));
//
////        System.out.println(list2.get(0).toString());
////        System.out.println(list2.get(1).toString());
//        String a = list2.get(0).toString();
//        String b = list2.get(1).toString();
//        cost = 0;
//        resLen = a.length();
//        for(i=0; i<resLen; i++){
//            if(a.charAt(i) == '_' || b.charAt(i) == '_'){
//                cost += 30;
//            }
//            else{
//                cost += efAlign.mismatchCost.get(new StringBuilder().append(a.charAt(i)).append(b.charAt(i)).toString());
//            }
//        }
////        System.out.println("Efficient version final cost: "+cost);
////        System.out.println("\n\n");



        //DCAlign Ver.2

        efAlign.initDcAlign(A, B);

        cpuTimeAfter = stat3.getCurrentThreadCpuTime()/1000000000.0;

        memoryUsageAfter = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

        cost = 0;
        resLen = efAlign.align[0].length();
        for(i=0; i<resLen; i++){
            if(efAlign.align[0].charAt(i) == '_' || efAlign.align[1].charAt(i) == '_'){
                cost += 30;
            }
            else{
                cost += efAlign.mismatchCost.get(new StringBuilder().append(efAlign.align[0].charAt(i)).append(efAlign.align[1].charAt(i)).toString());
            }
        }


        File fout = new File("output.txt");
        if(fout.exists()){
            fout.delete();
        }
        fout.createNewFile();
        BufferedWriter output = new BufferedWriter(new FileWriter(fout));
        output.write(efAlign.align[0].substring(0, Math.min(50, efAlign.align[0].length())) + " " + efAlign.align[0].substring(Math.max(0, efAlign.align[0].length() - 50), efAlign.align[0].length()) + "\n");
        output.write(efAlign.align[1].substring(0, Math.min(50, efAlign.align[0].length())) + " " + efAlign.align[1].substring(Math.max(0, efAlign.align[0].length() - 50), efAlign.align[0].length()) + "\n");
        output.write(String.valueOf((double)cost) + "\n");
        //memory
        output.write(String.valueOf((memoryUsageAfter-memoryUsageBefore)/(1024.0)) + "\n");
        //time
        output.write(String.valueOf(cpuTimeAfter-cpuTimeBefore));
        output.close();

    }
}