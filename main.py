from view_model import SuspeitoViewModel
from view import SuspeitoView


if __name__ == "__main__":
    vm = SuspeitoViewModel()
    view = SuspeitoView(vm)
    view.iniciar()