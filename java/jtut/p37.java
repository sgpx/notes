import java.io.File;


class p37 {
	public static void main(String[] args){
		try {
			File file = new File("/Users/sp/prog/notes/java/jtut/tmp.txt");	
			String[] paths = file.list();
			System.out.println(paths.length);
			for(String x : paths)
			{
				System.out.println(x);
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
}
