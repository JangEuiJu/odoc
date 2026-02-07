import java.io.*;
import java.math.BigInteger;
import java.util.*; 
public class Main {	
    public static void main(String[] args) throws Exception {		
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));        
        StringTokenizer st = null;        
        st = new StringTokenizer(br.readLine());                
        int n = Integer.parseInt(st.nextToken());        
        for(int i=0; i<n; i++) {        	
            st = new StringTokenizer(br.readLine());        	
            String s = st.nextToken();        	
            BigInteger a = new BigInteger(s);        	        	
            String res = "NO";        	        	
            StringBuilder sb = new StringBuilder();        	
            for(int j=s.length()-1; j>=0; j--)        		
                sb.append(s.charAt(j));        	      	
            BigInteger b = new BigInteger(sb.toString());        	    		
            BigInteger left = new BigInteger("0");    		
            BigInteger right = new BigInteger("1000000000");    		    		
            boolean flag1 = false;    		
            while(left.compareTo(right) != 1) {     			
                BigInteger mid = left.add(right).divide(new BigInteger("2"));    			
                if(mid.pow(2).compareTo(a) == 0) {    				
                    flag1 = true;    				
                    break;    			
                } 
                else if(mid.pow(2).compareTo(a) == -1) {    				
                    left = mid.add(new BigInteger("1"));    			
                } else {    				
                    right = mid.subtract(new BigInteger("1"));    			
                }    		
            }    		    		
            if(flag1) {    			
                left = new BigInteger("0");        		
                right = new BigInteger("1000000000");        		        		
                while(left.compareTo(right) != 1) {         			
                    BigInteger mid = left.add(right).divide(new BigInteger("2"));        			
                    if(mid.pow(2).compareTo(b) == 0) {        				
                        res = "YES";        				
                        break;        			
                    } else if(mid.pow(2).compareTo(b) == -1) {        				
                        left = mid.add(new BigInteger("1"));        			
                    } else {        				
                        right = mid.subtract(new BigInteger("1"));        			
                    }        		
                }    		
            }        	
            System.out.println(res);        
        }    
    }
}
