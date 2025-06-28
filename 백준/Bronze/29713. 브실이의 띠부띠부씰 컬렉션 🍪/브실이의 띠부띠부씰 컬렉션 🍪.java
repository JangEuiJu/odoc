import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<String, Integer> dict=new HashMap<>();
        int n=Integer.parseInt(br.readLine());
        String a=br.readLine();
        dict.put("B",0); dict.put("R",0); dict.put("O",0);
        dict.put("Z",0); dict.put("E",0); dict.put("S",0);
        dict.put("I",0); dict.put("L",0); dict.put("V",0);

        for(int i=0; i<n; i++){
            String temp=String.valueOf(a.charAt(i));
            if(dict.get(temp)!=null){
                dict.replace(temp, dict.get(temp)+1);
            }
        }

        ArrayList<String> arr=new ArrayList<>(dict.keySet());
        int min=1000;
        for(int i=0; i<arr.size(); i++){
            if(arr.get(i).equals("E") || arr.get(i).equals("R")){
                min= min > dict.get(arr.get(i))/2 ? dict.get(arr.get(i))/2 :min;
            }
            else{
                min= min > dict.get(arr.get(i)) ? dict.get(arr.get(i)) : min;
            }
        }

        bw.write(min+"");
        bw.flush();
    }
}