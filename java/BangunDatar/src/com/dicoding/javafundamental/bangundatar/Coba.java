package com.dicoding.javafundamental.bangundatar;
import java.io.File;
import java.io.FileReader;
public class Coba {
    public  static void  main(String[] args){
        int input = 3;
        switch (input) {
            case 1:
                System.out.println("1");
                break;
            case 2:
                System.out.println("2");
                break;
            case 3:
                System.out.println("3");
                break;
            case 4:
                System.out.println("4");
                break;
            default:
                break;
        }
        for (int i=0;i<5;i++){
            System.out.println(i);
        }
        int g = 9;
        int h = 2;
        System.out.println(g % h);
        int grade = -75;
        if (grade < 75) {
            System.out.println("Tidak lulus");
        } else if (grade == 75) {
            System.out.println("Belajar lebih giat lagi");
        } else {
            System.out.println("Pertahankan");
        }
        int T = 30;

        if (T < 0) {
            System.out.println("Wujud air adalah beku " + T);
        } else if ((0 <= T) && (T <= 100)) {
            System.out.println("Wujud air adalah cair " + T);
        } else if (T > 100) {
            System.out.println("Wujud air berupa gas atau uap " + T);
        }
        int l = 4;
        double z =(double)l ;
    }
}

