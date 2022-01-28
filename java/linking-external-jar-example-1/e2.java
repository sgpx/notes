import org.apache.commons.math.Field;
class foo implements Field<Integer> {
	public Integer getZero() { return 0; }
	public Integer getOne() { return 1; }
}

class e2 {
	public static void main(String[] args){
		foo f1 = new foo();
		System.out.println(f1.getZero());
		System.out.println(f1.getOne());
		System.out.println("OK");
	}
}
