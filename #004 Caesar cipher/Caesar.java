import java.util.Arrays;

public class Caesar{
    private static char[] caesar(char[] c, int shift){
        for(int i=0;i<c.length;i++){
            // can either choose aschii values as the boundaries or the characters themselves
            if(c[i] >= 'A' && c[i] <= 'Z'){
                // we are dealing with capital letters
                c[i] = (char) ((((int) (c[i] - 65 + shift)) % 26) + 65);
            }
            else if(c[i] >= 'a' && c[i] <= 'z'){
                // we are dealing with lowercase letters
                c[i] = (char) ((((int) (c[i] - 97 + shift)) % 26) + 97);
            }
        }

        return c;
    }

    public static void main(String[] args){
        System.out.println(Arrays.toString(caesar(args[0].toCharArray(), Integer.parseInt(args[1]))));
    }
}