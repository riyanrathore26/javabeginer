import java.util.*;
//import java.Scanner.*;
class FirstLinkedlist
{
	public static  void main(String args[])
	{
		LinkedList<Integer> ll =new LinkedList<Integer>();
		Scanner sc=new Scanner(System.in);
		System.out.println("please entrer value");
		int num=sc.nextInt();
		while(num>0){
		ll.add(sc.nextInt());
		num--;
		}
		System.out.println(ll);
	}
}
