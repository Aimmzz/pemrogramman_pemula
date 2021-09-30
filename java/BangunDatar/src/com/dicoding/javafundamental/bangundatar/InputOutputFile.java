package com.dicoding.javafundamental.bangundatar;

import java.io.File;
import java.io.FileReader;

public class InputOutputFile {
    public static void main(String[] args){
        try {
            File file = new File("D://Test.txt");
            FileReader fr = new FileReader(file);
            System.out.println("Read File Berhasil");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
