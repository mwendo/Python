class SLNode{
    constructor(val){
        this.val = val;
        // Pointer to next node
        this.next = null;
    }
}

class SLL{
    constructor(){
        this.next = null;
        this.head = null;
    }


    // Create method to add a SLNode to the end of the list.
    addBack(val){
        var node =  new SLNode(val);

        if(this.head == null){
            this.head = node;
            return this;
        }

        // Iterate to get to the end of the list.
        var runner = this.head;
        while(runner.next){
            runner = runner.next;
        }

        // Adding to the end of the list.
        runner.next = node;
        return this;

    }

    listNode(val, after) {
        this.val = val;
        this.next = null;

        if(this.next = null){
            this.head = node;
            return this;
        }
    }


    printVals(){

        var runner = this.head;
        while(runner){
            console.log(runner.val);
            runner = runner.next
        }
    }

    prepend(val,before) {
        val = new SLNode(val);
        if (this.head==null) {
            this.head = val;
            return this;
        }

        var runner = this.head;
        while (runner!=null) {
            if (runner.next.val==before) {
                var temp = runner.next;
                runner.next = val;
                val.next = temp;
                return this;
            }
            if (runner.next==null) {
                runner.next = val;
                return this;
            }
            runner = runner.next;
        }
    }
    
}

var list = new SLL();

list.addBack(1);
list.addBack(2);
list.addBack(3);
list.addBack(4);
list.addBack(5);
list.prepend(10,4);
list.printVals();