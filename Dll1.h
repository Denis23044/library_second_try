// Приведенный ниже блок ifdef — это стандартный метод создания макросов, упрощающий процедуру
// экспорта из библиотек DLL. Все файлы данной DLL скомпилированы с использованием символа DLL1_EXPORTS
// Символ, определенный в командной строке. Этот символ не должен быть определен в каком-либо проекте,
// использующем данную DLL. Благодаря этому любой другой проект, исходные файлы которого включают данный файл, видит
// функции DLL1_API как импортированные из DLL, тогда как данная DLL видит символы,
// определяемые данным макросом, как экспортированные.
#include "../../../task2/Plate.h"
#include "../../../task2/ContactData.h"
#include "../../../task2/PowerContact.h"

#ifdef DLL1_EXPORTS
#define DLL1_API __declspec(dllexport)
#else
#define DLL1_API __declspec(dllimport)
#endif
/*
// Этот класс экспортирован из библиотеки DLL
class DLL1_API CDll1 {
public:
	
	CDll1(void);
	// TODO: добавьте сюда свои методы.
};

extern DLL1_API int nDll1;*/

DLL1_API int fnDll1(void);
#define DllExport __declspec(dllexport)
extern "C" {
	__declspec(dllexport) Plate* create_plate(double x1 = 0, double x2 = 0, double y1 = 0, double y2 = 0, int plateNumber = 1);
	__declspec(dllexport) void delete_plate(Plate* plate);
	__declspec(dllexport) int add_contact_data(Plate* plate, Device* device, int x = 0, int y = 0, int contact_num = 0, int plate_num = 0, const string& name = "def");
	__declspec(dllexport) int add_power_contact(Plate* plate, Device* device, int x = 0, int y = 0, int contact_num = 0, int plate_num = 0, double power = 0);
	__declspec(dllexport) int remove_contact(Plate* plate, int x, int y);
	__declspec(dllexport) void contact_info(Contact* contact);
	__declspec(dllexport) void plate_info(Plate* plate);
	__declspec(dllexport) Device* create_device(string name);
	__declspec(dllexport) void delete_device(Device* device);
};

