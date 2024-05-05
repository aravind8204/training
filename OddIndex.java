class OddIndex{
public static void main(String args[]){
  int a[]={2,1,3,4,5,2,5,24,24,2,1,0};
  int sum=0;
  for(int i=0;i<a.length;i++){
    if(i%2!=0){
      sum=sum+i;
    }
  }
  System.out.println(sum);
}
}
