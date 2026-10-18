import SwiftUI
struct ContentView: View {
    
    
    @State private var linkInput : String = ""
    
     private func doSomething () {
        print("linkInput is \(linkInput)")
        return
    }
    var body : some View {
        
        
        VStack(alignment: .leading){
            
            Text("foo : \(linkInput)")
                .font(.title)
                .foregroundColor(.white)
            TextField(
                "Link",
                text: $linkInput
            ).padding()
            Button("Submit", action: doSomething)
            
        }
        .padding()
        
    }
    
    
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
