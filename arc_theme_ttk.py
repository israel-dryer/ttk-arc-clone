"""
    This is a python translation of the tcl ARC theme derived from:
        https://github.com/cjrh/ttk-themes/blob/master/themes/arc/arc.tcl

    By Israel Dryer
    Created March 8, 2021
"""
from tkinter import ttk
import tkinter as tk
from pathlib import Path


COLORS = {
    'fg': '#5c616c',
    'bg': '#f5f6f7',
    'disabledbg': '#fbfcfc',
    'disabledfg': '#a9acb2',
    'selectbg': '#5294e2',
    'selectfg': '#ffffff',
    'window': '#ffffff',
    'focuscolor': '#5c616c',
    'checklight': '#fbfcfc'
}


def create_widget_layouts(style):
    """Create widget layouts for arc theme"""
    style.layout('TButton', [
        ('Button.button', {'children': [
            ('Button.focus', {'children': [
                ('Button.padding', {'children': [
                    ('Button.label', {'side': 'left', 'expand': '1'})]})]})]})])

    style.layout('Toolbutton', [
        ('Toolbutton.button', {'children': [
            ('Toolbutton.focus', {'children': [
                ('Toolbutton.padding', {'children': [
                    ('Toolbutton.label', {'side': 'left', 'expand': '1'})]})]})]})])

    style.layout('Vertical.TScrollbar', [
        ('Vertical.Scrollbar', {'children': [
            ('Vertical.Scrollbar.trough', {'sticky': 'ns', 'children': [
                ('Vertical.Scrollbar.thumb', {'expand': '1'})]})]})])

    style.layout('Horizontal.TScrollbar', [
        ('Horizontal.Scrollbar', {'children': [
            ('Horizontal.Scrollbar.trough', {'sticky': 'ew', 'children': [
                ('Horizontal.Scrollbar.thumb', {'expand': '1'})]})]})])

    style.layout('TMenubutton', [
        ('Menubutton.button', {'children': [
            ('Menubutton.focus', {'children': [
                ('Menubutton.padding', {'children': [
                    ('Menubutton.indicator', {'side': 'right'}),
                    ('Menubutton.label', {'side': 'right', 'expand': '1'})]})]})]})])

    style.layout('TCombobox', [
        ('Combobox.field', {'sticky': 'news', 'children': [
            ('Combobox.downarrow', {'side': 'right', 'sticky': 'ns', 'children': [
                ('Combobox.arrow', {'side': 'right'})]}),
            ('Combobox.padding', {'expand': '1', 'sticky': 'news', 'children': [
                ('Combo.textarea', {'sticky': 'news'})]})]})])

    style.layout('TSpinbox', [
        ('Spinbox.field', {'side': 'top', 'sticky': 'we', 'children': [
            ('Spinbox.buttons', {'side': 'right', 'children': [
                ('', {'side': 'right', 'children': [
                    ('Spinbox.uparrow', {'side': 'top', 'sticky': 'nse', 'children': [
                        ('Spinbox.symuparrow', {'side': 'right', 'sticky': 'e'})]}),
                    ('Spinbox.downarrow', {'side': 'bottom', 'sticky': 'nse', 'children': [
                        ('Spinbox.symdownarrow', {'side': 'right', 'sticky': 'e'})]})]})]}),
            ('Spinbox.padding', {'sticky': 'news', 'children': [
                ('Spinbox.textarea', {'sticky': 'news'})]})]})])


def load_images():
    return {file.stem: tk.PhotoImage(file.stem, file=file) for file in Path('./assets').iterdir()}


def create_elements(style):
    """Create new elements for arc theme"""
    style.element_create('Button.button', 'image', 'button',
                         ('pressed', 'button-active'),
                         ('active', 'button-hover'),
                         ('disabled', 'button-insensitive'),
                         border=3, padding=(3, 2), sticky='ewns')

    style.element_create('Toolbutton.button', 'image', 'button-empty',
                         ('selected', 'button-active'),
                         ('pressed', 'button-active'),
                         ('active !disabled', 'button-hover'),
                         border=3, padding=(3, 2), sticky='news')

    style.element_create('Checkbutton.indicator', 'image', 'checkbox-unchecked',
                         ('disabled', 'checkbox-unchecked-insensitive'),
                         ('active selected', 'checkbox-checked'),
                         ('pressed selected', 'checkbox-checked'),
                         ('active', 'checkbox-unchecked'),
                         ('selected', 'checkbox-checked'),
                         ('disabled selected', 'checkbox-checked-insensitive'),
                         width=22, sticky='w')

    style.element_create('Radiobutton.indicator', 'image', 'radio-unchecked',
                         ('disabled', 'radio-unchecked-insensitive'),
                         ('active selected', 'radio-checked'),
                         ('pressed selected', 'radio-checked'),
                         ('active', 'radio-unchecked'),
                         ('selected', 'radio-checked'),
                         ('disabled selected', 'radio-checked-insensitive'),
                         width=22, sticky='w')

    style.element_create('Horizontal.Scrollbar.trough', 'image', 'trough-scrollbar-horiz')

    style.element_create('Horizontal.Scrollbar.thumb', 'image', 'slider-horiz',
                         ('pressed !disabled', 'slider-horiz-active'),
                         ('active !disabled', 'slider-horiz-prelight'),
                         ('disabled', 'slider-horiz-insens'),
                         border=6, sticky='ew')

    style.element_create('Vertical.Scrollbar.trough', 'image', 'trough-scrollbar-vert')

    style.element_create('Vertical.Scrollbar.thumb', 'image', 'slider-vert',
                         ('pressed !disabled', 'slider-vert-active'),
                         ('active !disabled', 'slider-vert-prelight'),
                         ('disabled', 'slider-vert-insens'),
                         border=6, sticky='ns')

    style.element_create('Horizontal.Scale.trough', 'image', 'trough-horizontal-active',
                         ('disabled', 'trough-horizontal'),
                         border=(8, 5, 8, 5), padding=0)

    style.element_create('Horizontal.Scale.slider', 'image', 'slider',
                         ('disabled', 'slider-insensitive'),
                         ('active', 'slider-prelight'))

    style.element_create('Vertical.Scale.trough', 'image', 'trough-vertical-active',
                         ('disabled', 'trough-vertical'),
                         border=(5, 8, 5, 8))

    style.element_create('Vertical.Scale.slider', 'image', 'slider',
                         ('disabled', 'slider-insensitive'),
                         ('active', 'slider-prelight'))

    style.element_create('Entry.field', 'image', 'entry-border-bg-solid',
                         ('focus', 'entry-border-active-bg-solid'),
                         ('disabled', 'entry-border-disabled-bg'),
                         border=3, padding=(6, 4), sticky='news')

    style.element_create('Labelframe.border', 'image', 'labelframe',
                         border=4, padding=4, sticky='news')

    style.element_create('Menubutton.button', 'image', 'button',
                         ('pressed', 'button-active'),
                         ('active', 'button-hover'),
                         ('disabled', 'button-insensitive'),
                         sticky='news', border=3, padding=(3, 2))

    style.element_create('Menubutton.indicator', 'image', 'arrow-down',
                         ('active', 'arrow-down-prelight'),
                         ('pressed', 'arrow-down-prelight'),
                         ('disabled', 'arrow-down-insens'),
                         sticky='e', width=20)

    style.element_create('Combobox.field', 'image', 'combo-entry',
                         ('readonly disabled', 'button-insensitive'),
                         ('readonly pressed', 'button-active'),
                         ('readonly focus', 'button-focus'),
                         ('readonly hover', 'button-hover'),
                         ('readonly', 'button'),
                         ('disabled', 'combo-entry-insensitive'),
                         ('focus', 'combo-entry-focus'),
                         ('hover', 'combo-entry'),
                         border=4, padding=(6, 0, 0, 0))

    style.element_create('Combobox.downarrow', 'image', 'combo-entry-button',
                         ('pressed', 'combo-entry-button-active'),
                         ('active', 'combo-entry-button-hover'),
                         ('disabled', 'combo-entry-button-insensitive'),
                         border=4, padding=(0, 10, 6, 10))

    style.element_create('Combobox.arrow', 'image', 'arrow-down',
                         ('active', 'arrow-down-prelight'),
                         ('pressed', 'arrow-down-prelight'),
                         ('disabled', 'arrow-down-insens'),
                         sticky='e', width=15)

    style.element_create('Spinbox.field', 'image', 'combo-entry',
                         ('focus', 'combo-entry-focus'),
                         border=4, padding=(6, 1, 1, 1), sticky='news')


    style.element_create('Spinbox.uparrow', 'image', 'up-background',
                         ('pressed', 'up-background-active'),
                         ('active', 'up-background-hover'),
                         ('disabled', 'up-background-disable'),
                         width=20, border=(0, 2, 3, 0), padding=(0, 5, 6, 2))

    style.element_create('Spinbox.symuparrow', 'image', 'arrow-up-small',
                         ('active', 'arrow-up-prelight'),
                         ('pressed', 'arrow-up-small-prelight'),
                         ('disabled', 'arrow-up-small-insens'))

    style.element_create('Spinbox.downarrow', 'image', 'down-background',
                         ('pressed', 'down-background-active'),
                         ('active', 'down-background-hover'),
                         ('disabled', 'down-background-disable'),
                         width=20, border=(0, 0, 3, 2), padding=(0, 2, 6, 5))

    style.element_create('Spinbox.symdownarrow', 'image', 'arrow-down-small',
                         ('active', 'arrow-down-small-prelight'),
                         ('pressed', 'arrow-down-small-prelight'),
                         ('disabled', 'arrow-down-small-insens'))

    style.element_create('Notebook.client', 'image', 'notebook', border=1)

    style.element_create('Notebook.tab', 'image', 'tab-top',
                         ('selected', 'tab-top-active'),
                         ('active', 'tab-top-hover'),
                         padding=(0, 2, 0, 0), border=2)

    style.element_create('Horizontal.Progressbar.trough', 'image', 'trough-progressbar_v',
                         border=(5, 1, 5, 1), padding=1)

    style.element_create('Horizontal.Progressbar.pbar', 'image', 'progressbar_v',
                         border=(4, 0, 4, 0))

    style.element_create('Vertical.Progressbar.trough', 'image', 'trough-progressbar',
                         border=(1, 5, 1, 5), padding=1)

    style.element_create('Vertical.Progressbar.pbar', 'image', 'progressbar',
                         border=(0, 4, 0, 4))

    style.element_create('Treeview.field', 'image', 'treeview', border=1)

    style.element_create('Treeheading.cell', 'image', 'notebook',
                         ('pressed', 'notebook'),
                         border=1, padding=4, sticky='ewns')

    style.element_create('Treeitem.indicator', 'image', 'plus',
                         ('user2', 'empty'),
                         ('user1', 'minus'),
                         width=15, sticky='w')


def create_widget_styles(style):
    """Create styles for each widget"""
    style.map('.', background=[('disabled', COLORS['disabledfg'])])

    style.configure('.',
                    background=COLORS['bg'],
                    foreground=COLORS['fg'],
                    troughcolor=COLORS['bg'],
                    selectbg=COLORS['selectbg'],
                    selectfg=COLORS['selectfg'],
                    fieldbg=COLORS['window'],
                    font=('TkDefaultFont',),
                    borderwidth=1,
                    focuscolor=COLORS['focuscolor']
                    )

    style.configure('TButton', padding=(8, 4, 8, 4), width=10, anchor='center')

    style.configure('TMenubutton', padding=(8, 4, 4, 4))

    style.configure('Toolbutton', anchor='center')

    style.map('TCheckbutton', background=[('active', COLORS['checklight'])])
    style.configure('TCheckbutton', padding=3)

    style.map('TRadiobutton', background=[('active', COLORS['checklight'])])
    style.configure('TRadiobutton', padding=3)

    style.configure('TNotebook', tabmargins=(0, 2, 0, 0))
    style.configure('TNotebook.Tab', padding=(6, 2, 6, 2), expand=(0, 0, 2))
    style.map('TNotebook.Tab', expand=[('selected', (1, 2, 4, 2))])

    style.configure('TSeparator', background=COLORS['bg'])

    style.configure('Treeview', background=COLORS['window'])
    style.configure('Treeview.Item', padding=(2, 0, 0, 0))
    style.map('Treeview',
              background=[('selected', COLORS['selectbg'])],
              foreground=[('selected', COLORS['selectfg'])])


def themed_style():
    style = ttk.Style()
    style.theme_create('izzy-arc', 'default')
    style.theme_use('izzy-arc')
    style.images = load_images()
    create_widget_layouts(style)
    create_elements(style)
    create_widget_styles(style)
    return style
