import SwiftUI
struct ContentView: View {
    var body : some View {
        VStack(alignment: .leading){
            Text("foo")
                .font(.title)
                .foregroundColor(.white)
            Text("Blah")
                .font(.title).foregroundColor(.white)
            Image("test-image-1")
                .fixedSize()
            
        }
        .padding()
        
    }
    
    
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
