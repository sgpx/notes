class FreshJuice {
	enum FreshJuiceSize { SMALL, MEDIUM, LARGE };
	FreshJuiceSize size;
}

public class p02 {
	public static void main(String[] args){
		FreshJuice j = new FreshJuice();
		j.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println(j.size);
	}
}
