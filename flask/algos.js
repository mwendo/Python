class SLNode{
    cosntructor(val){
        this.val = val;
        // Pointer to next node
        this.next = next;
    }
}

class  SLL{
    constructor(){
        this.head = null;

    addBack(val) {
        var node = new SLNode(val);

        if(this.head == null){
            this.head = node;
            return this;
        }
        
        var runner = this.head;
        while(runner.next){
            console.log(runner.val);
            runner = runner.next
        }
    }

}

