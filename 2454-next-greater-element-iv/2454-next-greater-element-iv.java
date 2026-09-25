class stack{
    int[]arr;
    int top=-1;

    stack(int n){
     this.arr=new int[n];
    }
    void push(int v){
        top+=1;
        this.arr[top]=v;
    }
    int pop(){
        return this.arr[this.top--];
    }
    boolean has(){
        return this.top>=0;
    }
    int peek(){
        return this.arr[this.top];
    }
    int size(){
        return this.top+1;
    }
}
class Solution {

    public int[] secondGreaterElement(int[] nums) {
        int n=nums.length;
        var s1=new stack(n);
        var s2=new stack(n);
        var ans=new int[n];
        Arrays.fill(ans,-1);

        for(int i=0;i<n;i++){
            while (s2.has() && nums[s2.peek()]<nums[i])
                 ans[s2.pop()]=nums[i];

            var temp=new stack(s1.size());

            while (s1.has() && nums[s1.peek()]<nums[i])
                 temp.push(s1.pop());
            
            while(temp.has())
                s2.push(temp.pop());
            s1.push(i);

        }
        return ans;

    }
}