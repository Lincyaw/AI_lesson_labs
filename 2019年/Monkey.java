/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package monkey;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 *
 * @author admin
 */
public class Monkey {

    class State{
        Character monkey; //猴子的位置
        Character box;   //盒子的位置
        int on;  //是否在盒子上
        int getbanana; //是否摘到香蕉
        int no;     //当前状态的序号
        String op;  //操作

        public State(char monkey, char box, int onbox, int banana, int no, String op) {
            this.monkey = monkey;
            this.box = box;
            this.on = onbox;
            this.getbanana = banana;
            this.no = no;
            this.op = op;           //进行了什么操作
        }
        public State(){
            
        }

        @Override
        public String toString() {
            return "State{" + "monkey=" + monkey + ", box=" + box + ", on=" + on + ", getbanana=" + getbanana+"}";
        }
        
        
        
    }
   
   boolean flag = false;    //手中无香蕉
   private int num = 0;     //用来给一个状态编序号
   int[] record  = new int[100];  //用来记录某个状态的上一个状态，方便回溯找到到这一步的路径
   Queue<State> queue = new LinkedList();
   ArrayList<State> StateList = new ArrayList<>();//用来保存所有尝试过的状态
   
   /**
    * 进行记录
    */
   public void Record(State next,int pre){
       this.StateList.add(this.num, next);
       this.record[this.num] = pre;  //记录路径，state.no为上一个状态
       this.queue.add(next);         //将该状态加入队列
       System.out.println("新状态进入队列-"+next.toString()); 
   }
   /**
    * 猴子向某一处移动
    * @param state 
    */
   
   public void Move(State state){
       State next  = null;
       if(state.on == 0){
           if(state.monkey == 'A'){
               next = new State('B',state.box,0,0,++num,"Move from A to B");    //新状态猴子从A走向B
               
           }
           else if(state.monkey == 'B'){
               next = new State('A',state.box,0,0,++num,"Move from B to A");    //新状态猴子从B走向A
           }
       }
     if(next!=null){
         Record(next,state.no);
     }
   }
   /**
    * 推箱子
    * @param state 
    */
   public void push(State state){
       //推箱子的条件：猴子与盒子在同一个地方,手上没有香蕉，猴子没站在箱子上
       State next = null;
       if(state.monkey.equals(state.box)&&state.on==0&&state.getbanana==0){
           //只要能推盒子在任意地方都推向C
           next = new State('C','C',0,0,++num,"pushBox from"+state.box.toString()+"to C");
       }
       if (next!=null){
           Record(next, state.no);
       }
   }
   /**
    * 是否能爬上箱子
    * @param state 
    */
   public void Climb(State state){
       State next = null;
       //猴子和箱子在同一个地方，并且猴子不站在箱子上
       if(state.monkey.equals(state.box)&&state.on==0){
           next = new State(state.monkey,state.box,1,0,++num,"Climb");
       }
       if (next!=null){
           Record(next, state.no);
       }
   }
   /**
    * 猴子得到香蕉
    * @param state 
    */
   public void Get(State state){
       State next = null;
       //猴子在C，箱子在C，猴子站在箱子上，猴子还没摘到香蕉
       if(state.box=='C'&&state.monkey=='C'&&state.on==1&&this.flag==false){
           next = new State('C','C',1,1,++num,"Get");
           this.flag = true;
       }
       if (next!=null){
           Record(next, state.no);
       }
   }
   /**
    * 广度优先搜索，寻找解决方案
    */
   public void findSolution(){
       State start = new State('A','B',0,0,num,"start");
       this.StateList.add(0,start);
       this.queue.add(start);
       System.out.println("新状态进入队列-"+start.toString());
       while(!queue.isEmpty()){
           State now = queue.poll();
           System.out.println("队列中删除状态-"+now.toString());
           Move(now);
           push(now);
           Climb(now);
           Get(now);
           if(this.flag){
               break;
           }
       }
       if(this.flag==false){
           System.out.println("impossible");
           return;
       }
       
       Stack<Integer> stack = new Stack();
       int now = this.num;      //结束状态的序号
       stack.push(now);                   
       while(now!=0){
           int pre = record[now];
           stack.push(pre);
           now = pre;
       }
       
       System.out.println("\n\n");
       while(!stack.isEmpty()){
            now = stack.pop();
            State nowState = this.StateList.get(now);
            System.out.println(nowState.op);
            System.out.println("当前状态:"+nowState.toString());
            
       }
       
   }
    public static void main(String[] args) {
        Monkey test = new Monkey();
        test.findSolution();
    }
}
