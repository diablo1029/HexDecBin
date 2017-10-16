import java.util.Scanner;
public class BinPower {
	
	public BinPower() {
		
	}
	public void setBinary() {
	

		Scanner input= new Scanner(System.in);
		String name = "";
		String nums = "";
		String exs = "";
		int ans = 0;
		int num;
		int exp1;
		System.out.println("Hello most amazing Java Student! What is your name?");
		name = input.nextLine();
		System.out.println("Hello " + name + ", please enter a number.");
		nums = input.nextLine();
		num = Integer.parseInt(nums);
		System.out.println("Now, please enter a exponent for your number.");
		exs = input.nextLine();
		exp1 = Integer.parseInt(exs);
		ans = (int) Math.pow(num, exp1);	
		System.out.println("The number you entered was: " + num + ".\nThe exponent value was " + exp1 + " and the final number is " + ans);
		

	}
}