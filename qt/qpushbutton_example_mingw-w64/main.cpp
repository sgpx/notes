#include <QApplication>
#include <QWidget>
#include <QPushButton>

int main(int argc, char *argv[])
{

    QApplication app(argc, argv);

    QWidget window;
    QPushButton *quitBtn = new QPushButton("Quit", &window);
    quitBtn->setGeometry(50, 50, 50, 50);

    window.resize(300, 300);
    window.setWindowTitle("QPushButton");
    window.show();

    return app.exec();
}