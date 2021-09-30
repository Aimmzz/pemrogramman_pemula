package com.dicoding.javafundamental.array;

public class InisiasiArray {
    public static void main(String[] args) {
        int[] arrInt = new int[]{1, 2, 3, 4, 5, 6};
        // bisa juga : int[] arrInt = {1, 2, 3, 4, 5, 6};(disederhanakan)
        System.out.println(arrInt[0]);
        System.out.println(arrInt[1]);
        System.out.println(arrInt[2]);
        System.out.println(arrInt[3]);
        System.out.println(arrInt[4]);
        System.out.println(arrInt[5]);
        /*Selanjutnya cara kedua dengan melakukan inisiasi array per elemen.
         Ubahlah kode di dalam kelas InisiasiArraymenjadi seperti ini*/
        int[] arrIntt = new int[6];
        arrIntt[0] = 1;
        arrIntt[1] = 2;
        arrIntt[2] = 3;
        arrIntt[3] = 4;
        arrIntt[4] = 5;
        arrIntt[5] = 6;

        System.out.println(arrIntt[0]);
        System.out.println(arrIntt[1]);
        System.out.println(arrIntt[2]);
        System.out.println(arrIntt[3]);
        System.out.println(arrIntt[4]);
        System.out.println(arrIntt[5]);
    }
}
