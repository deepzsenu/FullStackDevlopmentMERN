
public class Hello{

    public static void conversions(){
        int a = 257;

        byte b = (byte)a;
        char c = 'A';
        int con = c;

        float f = 5.6f;
        int t = (int)f;

        System.out.println("byte "+ b);
        System.out.println("char to int : "+ con);
        System.out.println("Float to int : "+t);

    }
    public static void main(String[] args) {
        System.out.println("Hello World!");
        conversions();
    }
}