from scripts.template import NodeTemplate

class LinkState(NodeTemplate):
    def __init__(self, i, client_name, client_lable) -> None:
        super().__init__()
        self.client_name = client_name
        self.client_lable = client_lable

        self.__index = i

        self._json_nodes = None

    @property
    def json_nodes(self):
        if self._json_nodes == None:
            inject = self._inject(self.__index)
            random_delay = self._random_delay(self.__index)
            inject['wires'].append([random_delay['id']])
            check_link = self._check_link(self.__index)
            mqtt_out = self._mqtt_out(self.__index, self.client_name)
            random_delay['wires'].append([check_link['id'], mqtt_out['id']])
            link_state = self._link_state(self.__index, self.client_name, self.client_lable)
            swith = self._swith(self.__index)
            link_out = self._link_out(self.__index, x=1075, y=1300)
            check_link['wires'].append([link_state['id'], swith['id'], link_out['id']])
            link_in = self._link_in(self.__index, x=795, y=1160)
            link_in['wires'].append([mqtt_out['id'], check_link['id']])
            mqtt_in = self._mqtt_in(self.__index, self.client_name)
            delay_300ms = self._delay_300ms(self.__index)
            mqtt_in['wires'].append([delay_300ms['id']])
            delay_300ms['wires'].append([check_link['id']])
            self._json_nodes = [
                inject,
                random_delay,
                link_in,
                mqtt_out,
                mqtt_in,
                delay_300ms,
                check_link,
                link_state,
                swith,
                link_out,
            ]
        return self._json_nodes
