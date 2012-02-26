import imaplib
import gmail_imap

class gmail_mailboxes:
    
    def __init__(self, gmail_server):
        self.server = gmail_server
        self.mailboxes = list()

        
    def load(self):
        if(not self.server.loggedIn):
            self.server.login()
        
        for box in self.server.imap_server.list()[1]:
            name = box.split(' "/" ')[1][1:-1]
            if( name != "[Gmail]"):  #ignore global [Gmail] mailbox
                self.mailboxes.append(name)
                   
                   
    def __repr__(self):
        return "<gmail_mailboxes:  [%s]>" %  (',  '.join(self.mailboxes))
        
    def __getitem__(self, key): return self.mailboxes[key]
    def __setitem__(self, key, item): self.mailboxes[key] = item
    
    
    def rename_mailbox(self, oldmailbox, newmailbox):
        if(not self.server.loggedIn):
            self.server.login()
        rc, self.response = self.server.imap_server.rename(oldmailbox, newmailbox)
        return rc

    def create_mailbox(self, mailbox):
        if(not self.server.loggedIn):
            self.server.login()
        rc, self.response = self.server.imap_server.create(mailbox)
        return rc

    def delete_mailbox(self, mailbox):
        if(not self.server.loggedIn):
            self.server.login()
        rc, self.response = self.server.imap_server.delete(mailbox)
        return rc