import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.WindowConstants;
import javax.swing.SwingUtilities;
 
public class SimpleAlert implements Runnable {
    private JFrame f;
    public SimpleAlert(String myLabel)  {
        // Create the window
        f = new JFrame("Alert");
        // Sets the behavior for when the window is closed
        f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        // Add a layout manager so that the button is not placed on top of the label
        f.setLayout(new FlowLayout());
        // Add a label and a button
        f.add(new JLabel(myLabel));
    }

    @Override
    public void run() {
        // Arrange the components inside the window
        f.pack();
        // By default, the window is not visible. Make it visible.
        f.setVisible(true);
    }
 
    public static void main(String[] args) {
	String myLabel = "ALERT: ";

	for(int i = 0; i < args.length; i++)
		myLabel += args[i] + " ";

        SwingUtilities.invokeLater(new SimpleAlert(myLabel));
    }

}
