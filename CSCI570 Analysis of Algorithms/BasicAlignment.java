import java.util.ArrayList;
import java.util.HashMap;

public class BasicAlignment {

    private HashMap<String, Integer> mismatchCost = new HashMap<>();
    public ArrayList<StringBuilder> resArray = new ArrayList<>();
    private int gapPenalty = 30;

    private void createMismatchCostMap(){
        mismatchCost.put("AA", 0);   mismatchCost.put("AC", 110);   mismatchCost.put("AG", 48);   mismatchCost.put("AT", 94);
        mismatchCost.put("CA", 110);   mismatchCost.put("CC", 0);   mismatchCost.put("CG", 118);   mismatchCost.put("CT", 48);
        mismatchCost.put("GA", 48);   mismatchCost.put("GC", 118);   mismatchCost.put("GG", 0);   mismatchCost.put("GT", 110);
        mismatchCost.put("TA", 94);   mismatchCost.put("TC", 48);   mismatchCost.put("TG", 110);   mismatchCost.put("TT", 0);
    }

    public int SequenceAlign(String A, String B){
    	StringBuilder alignSeqA = new StringBuilder(), alignSeqB = new StringBuilder();
    	
        createMismatchCostMap();
        int aLen = A.length(), bLen = B.length(), i, j;
        int cost;
        int[][] opt = new int[aLen+1][bLen+1];
        for(i=0; i<aLen+1; i++){
            opt[i][0] = i*gapPenalty;
        }
        for(j=1; j<bLen+1; j++){
            opt[0][j] = j*gapPenalty;
        }

        //bottom-up dp
        for(i=1; i<aLen+1; i++){
            for(j=1; j<bLen+1; j++){
                opt[i][j] = Math.min(opt[i-1][j-1] + mismatchCost.get(new StringBuilder().append(A.charAt(i-1)).append(B.charAt(j-1)).toString()),
                        Math.min(opt[i-1][j] + gapPenalty, opt[i][j-1] + gapPenalty));
            }
        }

//        System.out.println("MinCost for basic: "+ opt[aLen][bLen]);

        //top-down solution construction
        for(i=aLen, j=bLen; i>=0 || j>=0; ){
            cost = opt[i][j];
            
            if(i==1 && j==0 && cost == gapPenalty){
                alignSeqA.insert(0,A.charAt(i-1));
                alignSeqB.insert(0,'_');
                i--;
            }else if(i==0 && j==1 && cost == gapPenalty) {
                alignSeqA.insert(0,'_');
                alignSeqB.insert(0,B.charAt(j-1));
                j--;
            }else if(i==0 && j==0) {
                i--;
                j--;
            }else if(i>=1 && j>=1 && cost == opt[i-1][j-1] + mismatchCost.get(new StringBuilder().append(A.charAt(i-1)).append(B.charAt(j-1)).toString())){
                alignSeqA.insert(0,A.charAt(i-1));
                alignSeqB.insert(0,B.charAt(j-1));
                i--;
                j--;
            }else if(i>=1 && cost == opt[i-1][j] + gapPenalty){
                alignSeqA.insert(0,A.charAt(i-1));
                alignSeqB.insert(0,'_');
                i--;
            }else if(j>=1 && cost == opt[i][j-1] + gapPenalty){
                alignSeqA.insert(0,'_');
                alignSeqB.insert(0,B.charAt(j-1));
                j--;
            }
        }

        resArray.add(alignSeqA);
        resArray.add(alignSeqB);

        return opt[aLen][bLen];
    }

}
