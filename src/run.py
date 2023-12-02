import multiprocessing
try:
    from nsuda_client.main import start_nsuda
except Exception as e:
    print(e)
    print("Нажмите любую кнопку для продолжения")
    input()
if __name__ == "__main__":
    multiprocessing.freeze_support()
    start_nsuda()