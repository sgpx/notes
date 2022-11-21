import java.io.*;

class p35 {
	public static void main(String[] args) throws IOException {
		InputStreamReader cin = new InputStreamReader(System.in);
		try
		{
			char c = (char) cin.read();
			System.out.println(c);
			while(c != 'q')
			{
				c = (char) cin.read();
				System.out.println(c);		
			}
		}
		finally
		{
			cin.close();
		}
	}
}
