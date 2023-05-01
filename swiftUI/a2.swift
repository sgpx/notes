import SwiftUI
struct ContentView: View {
    var body : some View {
        Text("foo").padding()
            .font(.title)
            .foregroundColor(.green)
    }
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
