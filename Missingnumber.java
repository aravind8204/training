public class Missingnumber {

 public static void main (String[] args) {
    int n=13;
    int arr[]={1,2,3,4,6,5,8,9,11,10,13,7};
    int sum=(n*(n+1))/2;
    for(int i=0;i<n-1;i++){
      sum=sum-arr[i];
    }
    System.out.println(sum);
  }

}
