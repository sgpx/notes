import java.io.*;

class p36 {
	public static void main(String[] args) throws IOException {
		//InputStream f1 = new FileInputStream("p33.java");
		File f = new File("p34.java");
		InputStream f2 = new FileInputStream(f);

		int x = f2.read();
		char c = ' ';
		while(x != -1)
		{
			c = (char) x;
			System.out.printf("%c",c);
			x = f2.read();
		}

		f2.close();
	}
}
