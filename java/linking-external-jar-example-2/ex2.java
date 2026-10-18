
import com.google.common.base.Charsets;
import com.google.common.io.Files;
import java.io.File;
import java.io.IOException;
import java.util.List;

public class ex2 {

    public static void main(String[] args) throws IOException {

	try{

        String fileName = "src/main/resources/balzac.txt";
        
        List<String> lines = Files.readLines(new File(fileName), 
                Charsets.UTF_8);
        
        for (String line: lines) {
            System.out.println(line);
        }


	}
	catch(Exception e){
		System.out.println("Printing stack trace");
		e.printStackTrace();
	}
        
    }
}
