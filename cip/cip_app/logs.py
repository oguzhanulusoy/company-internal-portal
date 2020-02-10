import datetime
import cip_app.constants as constants

DEBUG = constants.DEBUG

def logging(trace):
    '''
    Dosya adını yerel tarih ile oluşturacağız. Kod tekrarı
    olmaması için bu aşamada tanımlanır.
    '''
    file_name = str(datetime.datetime.now().strftime("%x") + ".txt").replace('/', '.')

    '''
    projenin debug özelliği açık mı, kapalı mı diye kontrol etmemiz gerekli.
    eğer projenin debug özelliği açık ise asıl işimizi yapmamız gerekir.
    log dosyası var ise gelen bilgi, o dosyaya yazılır; aksi takdirde
    yeni bir log dosyası oluşturulur.
    '''
    if (DEBUG == True):
        try:
            with open(str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(trace) + " @ " + str(datetime.datetime.now()) + "\n" + str(lines_in_log_file))
        except:
            with open(str(file_name), "a") as log_file:
                log_file.write(str(trace) + " @ " + str(datetime.datetime.now()) + "\n")
        finally:
            log_file.close()
    else:
        otherwise_condition = "debug_notes.txt"
        with open(str(otherwise_condition), "a") as log_file:
            log_file.write(str("Debug is false @ " + datetime.date.now()) + "\n")

