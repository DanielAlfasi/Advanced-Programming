interface ActualDoer {
    void do1();

    void do2();
}

interface I {
    void doThis(ActualDoer doer);

    void doThat(ActualDoer doer);
}

class Test {
    public static void doItAll(ActualDoer doer) {
        I obj1 = new A();
        I obj2 = new B();

        obj1.doThat(doer);
        obj2.doThis(doer);
        obj1.doThis(doer);
        obj2.doThat(doer);
    }
}

abstract class abstractdoer implements I {
    @Override
    public void doThat(ActualDoer d) {
        d.do2();
        d.do1();
    }

    abstract public void doThis();
}

class A extends abstractdoer {
    public void doThis(ActualDoer d) {
        d.do1();
    }

}

class B implements I {
    public void doThis(ActualDoer d) {
        d.do2();
    }
}