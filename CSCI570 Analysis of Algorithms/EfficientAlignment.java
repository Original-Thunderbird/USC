import java.util.*;

public class EfficientAlignment {

    class Pair{
        int aInd, bInd;
        public Pair(int a, int b){
            aInd = a;
            bInd = b;
        }
    }

    public HashMap<String, Integer> mismatchCost = new HashMap<>();
    private ArrayList<StringBuilder> resArray = new ArrayList<>();
    public LinkedList<Pair> alignArray = new LinkedList<>();
    public String[] align = new String[2];
    private int gapPenalty = 30;

    private void createMismatchCostMap() {
        mismatchCost.put("AA", 0);
        mismatchCost.put("AC", 110);
        mismatchCost.put("AG", 48);
        mismatchCost.put("AT", 94);
        mismatchCost.put("CA", 110);
        mismatchCost.put("CC", 0);
        mismatchCost.put("CG", 118);
        mismatchCost.put("CT", 48);
        mismatchCost.put("GA", 48);
        mismatchCost.put("GC", 118);
        mismatchCost.put("GG", 0);
        mismatchCost.put("GT", 110);
        mismatchCost.put("TA", 94);
        mismatchCost.put("TC", 48);
        mismatchCost.put("TG", 110);
        mismatchCost.put("TT", 0);
    }

    public ArrayList<StringBuilder> SequenceAlign(String A, String B) {

    	StringBuilder alignSeqA = new StringBuilder(), alignSeqB = new StringBuilder();
        int aLen = A.length(), bLen = B.length(), i, j;
        long cost;
        int[][] opt = new int[aLen + 1][bLen + 1];
        for (i = 0; i < aLen + 1; i++) {
            opt[i][0] = i * gapPenalty;
        }
        for (j = 1; j < bLen + 1; j++) {
            opt[0][j] = j * gapPenalty;
        }

        //bottom-up dp
        for (i = 1; i < aLen + 1; i++) {
            for (j = 1; j < bLen + 1; j++) {
                opt[i][j] = Math.min(opt[i - 1][j - 1] + mismatchCost.get(new StringBuilder().append(A.charAt(i - 1)).append(B.charAt(j - 1)).toString()),
                        Math.min(opt[i - 1][j] + gapPenalty, opt[i][j - 1] + gapPenalty));
            }
        }

//        System.out.println("cost: "+ opt[aLen-1][bLen-1]);

        //top-down solution construction
        for (i = aLen, j = bLen; i >= 0 || j >= 0; ) {
            cost = opt[i][j];
            if (i == 1 && j == 0 && cost == gapPenalty) {
                alignSeqA.insert(0, A.charAt(i - 1));
                alignSeqB.insert(0, '_');
                i--;
            } else if (i == 0 && j == 1 && cost == gapPenalty) {
                alignSeqA.insert(0, '_');
                alignSeqB.insert(0, B.charAt(j - 1));
                j--;
            } else if (i == 0 && j == 0) {
                i--;
                j--;
            } else if (i >= 1 && j >= 1 && cost == opt[i - 1][j - 1] + mismatchCost.get(new StringBuilder().append(A.charAt(i - 1)).append(B.charAt(j - 1)).toString())) {
                alignSeqA.insert(0, A.charAt(i - 1));
                alignSeqB.insert(0, B.charAt(j - 1));
                i--;
                j--;
            } else if (i >= 1 && cost == opt[i - 1][j] + gapPenalty) {
                alignSeqA.insert(0, A.charAt(i - 1));
                alignSeqB.insert(0, '_');
                i--;
            } else if (j >= 1 && cost == opt[i][j - 1] + gapPenalty) {
                alignSeqA.insert(0, '_');
                alignSeqB.insert(0, B.charAt(j - 1));
                j--;
            }
        }
        resArray.clear();
        resArray.add(alignSeqA);
        resArray.add(alignSeqB);

        return resArray;
    }

    public int[] spaceEfficientAlign(String A, String B) {

    	createMismatchCostMap();
    	int m = B.length();
    	int n= A.length();
    	int[][] arr = new int[m+1][2];

    	for(int i=0; i<m+1; i++) {
    		arr[i][0] = i*gapPenalty;
    	}

    	for(int j=1; j<n+1;j++) {
    		arr[0][1] = j*gapPenalty;
    		for(int i=1;i<m+1;i++) {
    			arr[i][1] = Math.min(mismatchCost.get(new StringBuilder().append(A.charAt(j-1)).append(B.charAt(i-1)).toString()) 
    					+ arr[i-1][0], Math.min(arr[i-1][1]+gapPenalty, arr[i][0]+gapPenalty));
    		}
    		for(int i=0; i<m+1;i++) {
    			arr[i][0] = arr[i][1];
    		}
    	}

    	int[] res = new int[arr.length];
	    for(int i=0;i<arr.length;i++) {
	    	res[i] = arr[i][1];
	    }
    	return res;

    }

    public ArrayList<StringBuilder> DcAlign(String A, String B) {

    	int aLen = A.length();
    	int bLen = B.length();
    	int q = 0;
    	int minCost = Integer.MAX_VALUE;

    	String Ar = new StringBuilder().append(A).reverse().toString();
    	String Br = new StringBuilder().append(B).reverse().toString();

    	if(aLen<=2 || bLen<=2) {
    		return this.SequenceAlign(A, B);
    	}else {
    		int[] arrA = spaceEfficientAlign(A.substring(0, aLen/2), B);
    		int[] arrB = spaceEfficientAlign(Ar.substring(0, aLen/2), Br);
       		int len = arrA.length;
    		for(int i=0; i<len; i++) {
    			if(minCost > Math.min(minCost, arrA[i]+ arrB[len-i-1])) {
    				minCost = Math.min(minCost, arrA[i]+ arrB[len-i-1]);
    				q = i;
    			}
    		}

//    		System.out.println("MinCost for efficient: " + minCost);
    		ArrayList<StringBuilder> listleft = DcAlign(A.substring(0, aLen/2), B.substring(0,q));
    		StringBuilder listleftA = listleft.get(0);
    		StringBuilder listleftB = listleft.get(1);

    		ArrayList<StringBuilder> listright = DcAlign(A.substring(aLen/2, aLen), B.substring(q,bLen));
    		StringBuilder listrightA = listright.get(0);
    		StringBuilder listrightB = listright.get(1);

    		listleftA.append(listrightA);
    		listleftB.append(listrightB);
    		resArray.clear();
    		resArray.add(listleftA);
    		resArray.add(listleftB);
    	}
    	return resArray;

    }

    public void refinedSequenceAlign(String A, String B, int aStartInd, int bStartInd) {

        int aLen = A.length(), bLen = B.length(), i, j;
        long cost;
        int[][] opt = new int[aLen + 1][bLen + 1];
        for (i = 0; i < aLen + 1; i++) {
            opt[i][0] = i * gapPenalty;
        }
        for (j = 1; j < bLen + 1; j++) {
            opt[0][j] = j * gapPenalty;
        }

        //bottom-up dp
        for (i = 1; i < aLen + 1; i++) {
            for (j = 1; j < bLen + 1; j++) {
                opt[i][j] = Math.min(opt[i - 1][j - 1] + mismatchCost.get(new StringBuilder().append(A.charAt(i - 1)).append(B.charAt(j - 1)).toString()),
                        Math.min(opt[i - 1][j] + gapPenalty, opt[i][j - 1] + gapPenalty));
            }
        }

//        System.out.println("cost: "+ opt[aLen-1][bLen-1]);

        //top-down solution construction
        for (i = aLen, j = bLen; i + j > 1; ) {
            cost = opt[i][j];
//            if (i == 1 && j == 0 && cost == gapPenalty) {
////                alignSeqA.add(0, A.charAt(i - 1));
////                alignSeqB.add(0, '_');
//
//                alignment[0][aStartInd+i-1] = A.charAt(i - 1);
//                i--;
//            } else if (i == 0 && j == 1 && cost == gapPenalty) {
////                alignSeqA.add(0, '_');
////                alignSeqB.add(0, B.charAt(j - 1));
//
//                alignment[1][bStartInd+j-1] = B.charAt(j - 1);
//                j--;
//            } else if (i == 0 && j == 0) {
//                i--;
//                j--;
//            } else
                if (i >= 1 && j >= 1 && cost == opt[i - 1][j - 1] + mismatchCost.get(new StringBuilder().append(A.charAt(i - 1)).append(B.charAt(j - 1)).toString())) {
//                alignSeqA.add(0, A.charAt(i - 1));
//                alignSeqB.add(0, B.charAt(j - 1));
                    if((i-1)+(j-1) !=0) {
                        alignArray.add(new Pair(aStartInd + (i - 1), bStartInd + (j - 1)));
                    }
                i--;
                j--;
            } else if (i >= 1 && cost == opt[i - 1][j] + gapPenalty) {
//                alignSeqA.add(0, A.charAt(i - 1));
//                alignSeqB.add(0, '_');
                    if((i-1)+j != 0)  {
                        alignArray.add(new Pair(aStartInd+(i-1), bStartInd+j));
                    }
                i--;
            } else if (j >= 1 && cost == opt[i][j - 1] + gapPenalty) {
//                alignSeqA.add(0, '_');
//                alignSeqB.add(0, B.charAt(j - 1));
                    if(i+(j-1) != 0){
                        alignArray.add(new Pair(aStartInd+i, bStartInd+(j-1)));
                    }
                j--;
            }
        }
    }

    public void refinedDcAlign(String A, String B, int aStartInd, int bStartInd) {
        int aLen = A.length();
        int bLen = B.length();
        int q = 0;
        int minCost = Integer.MAX_VALUE;
//        String Ar = new StringBuilder().append(A).reverse().toString();
//        String Br = new StringBuilder().append(B).reverse().toString();
        ArrayList<ArrayList<Character>> res = new ArrayList<>();

        if (aLen <= 2 || bLen <= 2) {
//    		System.out.println("A is: "+ A);
//    		System.out.println("B is: "+ B);
            this.refinedSequenceAlign(A, B, aStartInd, bStartInd);
        } else {
            int mid = aLen/2;
            int[] arrA = spaceEfficientAlign(A.substring(0, mid), B);
            int[] arrB = spaceEfficientAlign(new StringBuilder().append(A.substring(mid, aLen)).reverse().toString(), new StringBuilder().append(B).reverse().toString());

            int len = arrB.length;

            for (int i = 0; i < len; i++) {
                if (minCost > arrA[i] + arrB[len - i - 1]) {
                    minCost = arrA[i] + arrB[len - i - 1];
                    q = i;
                }
            }
//            System.out.println("index added to alignment: A:" + (aStartInd+mid) + ", B: " + (bStartInd+q));

            alignArray.add(new Pair(aStartInd+mid, bStartInd+q));
            refinedDcAlign(A.substring(0, mid), B.substring(0, q), aStartInd, bStartInd); //q; mid or q+1; mid+1?
            refinedDcAlign(A.substring(mid, aLen), B.substring(q, bLen), aStartInd+mid, bStartInd+q);
        }
    }

    public void initDcAlign(String A, String B){
        int aLen = A.length(), bLen = B.length();

        alignArray.add(new Pair(0, 0));
        alignArray.add(new Pair(aLen, bLen));
        refinedDcAlign(A, B, 0, 0);

        Collections.sort(alignArray, new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                if (o1.aInd < o2.aInd) {
                    return -1;
                } else if (o1.aInd == o2.aInd) {
                    if (o1.bInd < o2.bInd) {
                        return -1;
                    } else if (o1.bInd == o2.bInd) {
                        return 0;
                    } else if (o1.bInd > o2.bInd) {
                        return 1;
                    }
                } else if (o1.aInd > o2.aInd) {
                    return 1;
                }
                return 0;
            }
        });

        int i, alignLen = alignArray.size();
        StringBuilder aAlignRes = new StringBuilder(), bAlignRes = new StringBuilder();

//        for(i=0; i<alignLen; i++){
//            System.out.print("(" + alignArray.get(i).aInd + "," + alignArray.get(i).bInd+"), ");
//        }
        for(i=0; i< alignLen-1; i++){
            if(alignArray.get(i+1).aInd - alignArray.get(i).aInd == 1 && alignArray.get(i+1).bInd - alignArray.get(i).bInd == 1){
                aAlignRes.append(A.charAt(alignArray.get(i).aInd));
                bAlignRes.append(B.charAt(alignArray.get(i).bInd));
            }
            else if(alignArray.get(i+1).aInd - alignArray.get(i).aInd == 0 && alignArray.get(i+1).bInd - alignArray.get(i).bInd == 1){
                aAlignRes.append('_');
                bAlignRes.append(B.charAt(alignArray.get(i).bInd));
            }
            else if(alignArray.get(i+1).aInd - alignArray.get(i).aInd == 1 && alignArray.get(i+1).bInd - alignArray.get(i).bInd == 0){
                aAlignRes.append(A.charAt(alignArray.get(i).aInd));
                bAlignRes.append('_');
            }
        }
        align[0] = aAlignRes.toString();
        align[1] = bAlignRes.toString();
    }
}
