import java.math.BigInteger;

public class Luhn{
    private static boolean luhn(String creditNumb){
        int sum = 0;
        for(int i=0; i<creditNumb.length();i++){
            int digit = Character.getNumericValue(creditNumb.charAt(i));
            if(i%2 !=0){
                digit = digit * 2;
                if(digit > 9){
                    digit -= 9;
                }
            }
            sum+= digit;
        }
        return (sum % 10 == 0);
    }

    public static void main(String[] args){
        String str = args[0];
        int length = str.length();
        boolean valid = luhn(str);
        long res = Long.parseLong(str.substring(0,2));
        if(valid && length == 15 && (res == 37 || res == 34)){
            System.out.println("AMEX\n");
        }
        else if(valid && length == 16 && (res >= 50 || res <= 55)){
            System.out.println("MASTERCARD\n");
        }
        else if(valid && (length == 16 || length == 13) && (Integer.parseInt(str.substring(1))) == 4){
            System.out.println("VISA\n");
        }
        else{
            System.out.println("INVALID\n");
        }
    }
}