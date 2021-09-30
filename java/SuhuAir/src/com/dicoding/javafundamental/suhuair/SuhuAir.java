package com.dicoding.javafundamental.suhuair;
import java.util.Scanner;

public class SuhuAir {
    public  static void main(String [] args){
        /* contoh pemakaian IF tiga kasus : wujud air */
        /*Kamus*/
        int T;
        /*Program*/
        System.out.println("Contoh IF tiga kasus");
        System.out.print("Suhu (der. c = ");
        //Scanner untuk masukan  suhu Air

        Scanner scanner = new Scanner(System.in);
        T = scanner.nextInt(); //masukan suhu air dengan tipe int
        //proses pengecekan if
        if (T < 0){
            System.out.println("Wujud Air Beku " + T);
        }else  if((0 <= T)&&(T <= 100)){
            System.out.println("Wujud Air cair " + T);
        }else if (T > 100){
            System.out.println("Wujud air uap/gas " + T);
        }

    }
}
