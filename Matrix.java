public class Metrix
{
    public static void main(String args[])
    {
       final int [][] Metrix={{1,2,3},{1,2,3},{1,2,3}};
        System.out.println("this is:");
        for(int i=0; i<Metrix.length; i++)
        {
            for(int j=0; j<Metrix[i].length;j++)
            {
                System.out.println(Metrix[i][j]+" ");
            }
            System.out.println();
        }
    }
}
