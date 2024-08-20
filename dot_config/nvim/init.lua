if os.getenv('TERM') == 'linux' then
  vim.o.bg = 'dark'
else
  vim.o.bg = 'light'
end
vim.o.nu = true
vim.o.rnu = true
vim.o.cursorline = true
vim.o.tabstop = 4
vim.o.shiftwidth = 2
vim.o.softtabstop = 2
vim.o.expandtab = true
vim.o.smartindent = true
vim.o.hlsearch = false
vim.o.incsearch = true
vim.o.scrolloff = 8
vim.o.updatetime = 50
vim.cmd.colorscheme('vim')
vim.o.tgc = false
vim.keymap.set('n', '<C-d>', '<C-d>zz')
vim.keymap.set('n', '<C-u>', '<C-u>zz')
vim.keymap.set('n', 'n', 'nzzzv')
vim.keymap.set('n', 'N', 'Nzzzv')
--vim.g.mapleader = " "
--vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
--vim.o.signcolumn = 'yes'
