import java.util.regex.Matcher;
import java.util.regex.Pattern;

class p24 {
	public static void main(String[] args){

		String line = "hey hey";
		String pattern = "^hey.+$";
		Pattern p = Pattern.compile(pattern);
		Matcher m = p.matcher(line);

		if(m.find())
		{
			System.out.println("Found value: " + m.group(0) );
		}
	}
}
