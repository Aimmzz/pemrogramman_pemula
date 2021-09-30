public class string {
    public static void main(String [] args){
    String greeting = "Hello World!";
    System.out.println(greeting);
    /*tipe data di java ada 8*/
        boolean value1 = true;
        boolean anotherValue1 = false;
        byte anotherValue = -10;
        short value2 = 15000;
        int value3 = 150000;
        long value4 = 150000L;
        float value5 = 3.5f;
        double value6 = 5.0;
        char item = 'A';
        System.out.println(anotherValue);
        System.out.println(anotherValue1);
        System.out.println(value1);
        System.out.println(value2);
        System.out.println(value3);
        System.out.println(value4);
        System.out.println(value5);
        System.out.println(value6);
        System.out.println(item);
        /*array*/
        char[] dicodingChars = { 'd', 'i', 'c', 'o', 'd', 'i', 'n', 'g' };
        String dicodingString = new String(dicodingChars);
        System.out.println(dicodingString);
        /*mengetahui panjang string menggunakan method length()*/
        String dicoding = "dicoding";
        int kami = dicoding.length();
        /*Mengambil Karakter Dari Sebuah String menggunakan method charAt(int index)*/
        char kamu = dicoding.charAt(7);
        System.out.println(kami);
        System.out.println(kamu);
}
}
