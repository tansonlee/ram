from ram import ram, ram_fetch, ram_store, core_dump

my_ram = ram_store(ram_store(ram, 77, 1010), 2, 999)
core_dump(my_ram)

my_ram_replace_2 = ram_store(my_ram, 2, 111)
core_dump(my_ram_replace_2)