package com.dicoding.javafundamental.percabangan;

public class coba {
    public  static void main(String[] args){
        int baju = 5000;
        int jumlah ;
        if (baju >= 5000){
            jumlah = 5;
        }else if (baju <= 4000){
            jumlah = 8;
        }else{
            jumlah = 90;
        }
        System.out.println("kamu " + jumlah);
    }
}
