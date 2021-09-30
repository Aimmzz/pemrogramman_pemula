package com.dicoding.javafundamental.accessmodifier.pacKage2;

import com.dicoding.javafundamental.accessmodifier.pacKage1.KelasA;

public class KelasB extends KelasA {

    @Override
    protected void methodC() {
        super.methodC();
        System.out.println("Contoh pemanggilan protected dari package luar");
    }
}
