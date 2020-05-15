class NotesStore {
    constructor(){
        this.notes = [];
    }

    addNote(state, name) {
        if(name == "") {
            throw new Error('Name cannot be empty');
        }

        var acceptedState = ["completed","active", "others"]
        if(!acceptedState.includes(state)) {
            throw new Error("invalid state " + state);
        }

        var note = {
            'name' : name,
            'state' : state
        }
        this.notes.push(note);

    }

    getNotes(state) {
        var acceptedState = ["completed","active", "others"]
        if(!acceptedState.includes(state)) {
            throw new Error("invalid state " + state);
        }

        var result = [];
        this.notes.map(function(note){
            if(note.state == state){
                result.push(note.name);
            }
        });

        return result;
    }
}


classA = new NotesStore()

console.log(classA.addNote('active','DrinkTea'))

console.log(classA.getNotes('active'));