public class sieve{
    public static boolean[] sieve(int n){
        boolean[] a = new boolean[n+1];
        for(int i=0;i<a.length;i++){
            a[i] = true;
        }

        for(int i=2;i<=Math.sqrt(n);i++){
            if(a[i] == true){
                System.out.println("i: " + String.valueOf(i));
                for(int j=i*i; j<=n; j=j+i){
                    System.out.println("j: " + String.valueOf(j));
                    a[j] = false;
                }
            }
        }

        return a;
    }

    public static void main(String[] args){
        int n = Integer.parseInt(args[0]);
        boolean[] a = sieve(n);
        String prefix = "";
        System.out.print("[");
        for(int i=2;i<a.length;i++){
            if(a[i] == true){
                System.out.print(prefix);
                System.out.print(String.valueOf(i));
                prefix = ", ";
            }
        }
        System.out.print("]");
    }
}