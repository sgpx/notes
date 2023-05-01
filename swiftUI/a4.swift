import SwiftUI
struct ContentView: View {
    
    @State private var textInput : String = ""
    var body : some View {
        
        
        VStack(alignment: .leading){
            
            Text("foo : \(textInput)")
                .font(.title)
                .foregroundColor(.white)
            TextField(
                "Link",
                text: $textInput
            ).padding()
                .onChange(of: textInput) { nv in
                    print("Name changed to \(textInput)! nv : \(nv)")
                }
            
        }
        .padding()
        
    }
    
    
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
