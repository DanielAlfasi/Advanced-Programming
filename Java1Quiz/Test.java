public class Test {
    static Foo x = new Bar();

    public static void main(String[] args) {
        Foo y = new Foo();
        Foo y1 = new Bar();
        Foo y2 = new Foo();
        Foo y3 = new Bar();
        Foo y4 = new Foo();
        Foo y5 = new Bar();
        Foo y6 = new Bar();
        Foo y7 = new Bar();

        System.out.println("a : " + Vars.a + " b : " + Vars.b + " c : " + Vars.c);
    }
}