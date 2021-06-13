import binwalk

def scan_recursively(filename):
    try:
        modules = binwalk.scan(filename, signature=True, matryoshka=True, extract=True, quiet=True)
        # for module in modules:
        #     for result in module.results:
        #         if result.file.path in module.extractor.output:
        #             # These are files that binwalk carved out of the original firmware image, a la dd
        #             if result.offset in module.extractor.output[result.file.path].carved:
        #                 print ("Carved data from offset 0x%X to %s" % (result.offset, module.extractor.output[result.file.path].carved[result.offset]))
        return modules
    except binwalk.ModuleException as e:
        print("Critical failure:", e)