import view
import model

def programm_run ():
    global inner_db
    choice = view.main_menu()
    if int(choice) == 1:
        inner_db = model.create_new_db_line(view.custom_input_rec(), model.global_mapping())
    elif int(choice) == 2:
        model.db_line_print(view.id_for_input())
    elif int(choice) == 3:
        inner_db = model.update_db_line(view.id_for_input(), view.custom_input_rec(), model.global_mapping())
    elif int(choice) == 4:
        inner_db = model.delete_line_by_ID(view.id_for_input())
    elif int(choice) == 5:
        model.export_to_file(view.file_name())
    elif int(choice) == 6:
        inner_db = model.import_from_db_with_id(view.file_name)
    elif int(choice) == 7:
        inner_db =  model.inner_base_from_list_of_dicts(model.import_without_id(model.row_parse(view.file_name)))
    elif int(choice) == 8:
        model.db_printing(inner_db)
    elif int(choice) == 9:
        quit()
    else: print('Неприемлемый пераметр ввода.')
    programm_run()
